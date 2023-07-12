from django.shortcuts import get_object_or_404, redirect, render
from .models import Customer, Order, OrderItem, Product
from django.http import JsonResponse
import json


def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store.html', context)

def product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        quantity = int(request.POST['quantity'])

        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # Update the quantity of the existing order item or create a new one
        orderItem.quantity = quantity
        orderItem.save()

        return redirect('store:cart')

    else:
        product = Product.objects.get(id=pk)
        context = {'product': product}
        return render(request, 'singleproduct.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def cart(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_items = order.orderitem_set.all()  # Retrieve all order items (products) associated with the order

    context = {'order': order, 'order_items': order_items}
    return render(request, 'cart.html', context)

    # Handle GET request without a specific product_id



def checkout(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        return redirect('checkout_complete')
    return render(request, 'checkout.html')


def order(request):
    return render(request, 'order.html')


def singleproduct(request):
    return render(request, 'singleproduct.html')
