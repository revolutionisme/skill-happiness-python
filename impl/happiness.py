from skill_sdk import skill, Response, ask, tell, context, Card
from skill_sdk.l10n import _
import requests
from random import randrange


@skill.intent_handler("TEAM_20_HAPPINESS")
def mood_handler():
    try:
        number = randrange(10)
        # TODO: add functionality to create personalized preferences, social/close friends group, to trigger a call.
        if number < 3:
            # TODO: Maybe add jokes in a database and source from there
            # Jokes sourced from "https://github.com/derphilipp/Flachwitze"
            response = requests.get('https://raw.githubusercontent.com/derphilipp/Flachwitze/master/README.md', timeout=10)
            raw_jokes = response.text.split("##")[1].split("\n")[2:]
            jokes = [j[2:] for j in raw_jokes]

            msg = _('HAPPINESS_JOKE', joke=jokes[randrange(len(jokes))])
            response = tell(msg)
        elif number < 6:
            # TODO: Add more URL's and if possible learn from user history
            video_ids = ["DODLEX4zzLQ","dQw4w9WgXcQ","tvMO9TNfdHs"]
            msg = _("HAPPINESS_CHECK_PHONE")
            response = tell(msg)
            response.card = Card(
                title=_("HAPPINESS_TITLE"),
                subtitle=_("HAPPINESS_SUB_TITLE"),
                action=f"https://www.youtube.com/watch?v={video_ids[randrange(len(video_ids))]}",
                actiontext=_("HAPPINESS_ACTION_TEXT")
            )
        else:
            msg = _("HAPPINESS_CHECK_PHONE")
            response = tell(msg)
            response.card = Card(
                title=_("HAPPINESS_TITLE"),
                subtitle=_("HAPPINESS_SUB_TITLE"),
                action=f"https://soundcloud.com/mariagrazia84/pharrell-williams-happy",
                actiontext=_("HAPPINESS_ACTION_TEXT")
            )
    except requests.exceptions.RequestException as err:
        msg = _('HAPPINESS_REQUEST_ERROR', err=err)
        response = tell(msg)

    # We create a response with either joke or error message
    return response



# Examples to extend the functionality to specific user, couldn't amke it work yet

# from skill_sdk.services.persistence import PersistenceService
# from skill_sdk import Response, ask, skill, context
# @skill.intent_handler('MY_BEST_INTENT_EVER')
# def handle_invoke() -> Response:
#     session_id = PersistenceService().get()['session_id']
#     if not session_id:
#         PersistenceService().set({'session_id': context.session.session_id})
#         return ask("Hey, first time here? What's your name?")
#     # Do whatever you want with user, that has already listened to intro
#     ...

# context_attr = context.attributesV2
# print(f"Context attributes - {context_attr}")
# session_id = context.session and context.session.session_id
# print(session_id)
