from budget.models import Item
from .models import ItemClone
from budget.models import Sheet

def object_assigner(request,sheet):
    object_list = Item.objects.filter(user = request.user)
    item_list = []
    counter = 0
    for i in object_list:
        item = ItemClone()
        og = object_list[counter]
        item.user = request.user
        item.title = og.title
        item.amount = og.amount
        item.tags = og.tags
        item.id_filter = sheet.id
        item.sheet = Sheet.objects.get(id = sheet.id)
        item.save()
        item_list.append(item)
        counter+=1
    return item_list


def del_items(request):
    for item in Item.objects.filter(user = request.user):
        item.delete()