from users.models import Action
import datetime

def create_timestamp():
    d = f'{datetime.datetime.now()}'
    old_format = f'%Y-%m-%d %H:%M'
    new_format = f'%m/%d/%Y %I:%M%p'
    date = datetime.datetime.strptime(d[0:16], old_format).strftime(new_format)
    timestamp = datetime.datetime.strptime(date, new_format)
    return timestamp

def create_date():
    d = f'{datetime.datetime.now()}'
    old_format = f'%Y-%m-%d'
    new_format = f'%m/%d/%Y'
    date = datetime.datetime.strptime(d[0:10], old_format).strftime(new_format)
    return date

def create_action(user, description):
    timestamp = create_timestamp()

    try:
        Action.objects.get(timestamp=timestamp)
    except:
        action = Action(user=user, 
                action=description, 
                timestamp=timestamp)
        return action.save()