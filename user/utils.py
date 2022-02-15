from budget.models import Item
from .models import ItemClone

def object_assigner(request):
    object_list = Item.objects.all()
    item_list = []
    counter = 0
    for i in object_list:
        item = ItemClone()
        og = object_list[counter]
        item.user = request.user
        item.title = og.title
        item.amount = og.amount
        item.tags = og.tags
        item.save()
        item_list.append(item)
        counter+=1
    return item_list


def del_items():
    for item in Item.objects.all():
        item.delete()