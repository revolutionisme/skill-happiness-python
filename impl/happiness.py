from skill_sdk import skill, Response, ask, tell
from skill_sdk.l10n import _
import requests
from random import randrange


@skill.intent_handler("TEAM_20_HAPPINESS")
def mood_handler():
    """
    :return:
    """
    try:
        number = randrange(10)

        if number < 3:
            # We request a random joke from icndb with time-out set to 10 seconds
            response = requests.get('http://api.icndb.com/jokes/random', timeout=10)
            # We parse the response json or raise exception if unsuccessful
            response.raise_for_status()
            data = response.json()
            # We get the joke from the response data
            joke = data['value']['joke'] if data.get('type') == 'success' else None
            # We format our response to user or ask for an excuse
            if joke:
                msg = _('HAPPINESS_JOKE', joke=joke)
            else:
                msg = _('HAPPINESS_RESPONSE_ERROR')
        elif number < 6:
            msg = _("HAPPINESS_YOUTUBE_VIDEO", video_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            msg = _("HAPPINESS_SONG", song_link="https://soundcloud.com/mariagrazia84/pharrell-williams-happy")
    except requests.exceptions.RequestException as err:
        msg = _('HAPPINESS_REQUEST_ERROR', err=err)

    # We create a response with either joke or error message
    return tell(msg)
