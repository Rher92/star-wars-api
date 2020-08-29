from api.models import Characters


def retrieve_character(cid):
    return Characters.objects.filter(cid=cid).first()
    