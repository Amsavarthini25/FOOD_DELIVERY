@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    data = request.data
    items = data.get('items', [])  # List of item dictionaries: [{"id": 1, "quantity": 2}, ...]

    if not items:
        return Response({'error': 'No items selected'}, status=400)

    total_price = 0
    unavailable_items = []

    # Check food availability
    for item in items:
        item_id = item.get('id')
        quantity = item.get('quantity', 1)  # Default to 1 if not provided

        food_item = get_object_or_404(FoodItem, id=item_id)
        
        if food_item.stock >= quantity:
            total_price += float(food_item.price) * quantity
        else:
            unavailable_items.append(f"{food_item.name} (Only {food_item.stock} available)")

    if unavailable_items:
        return Response({'error': f"These items are unavailable: {', '.join(unavailable_items)}"}, status=400)

    # Deduct stock for ordered items
    for item in items:
        item_id = item.get('id')
        quantity = item.get('quantity', 1)

        food_item = get_object_or_404(FoodItem, id=item_id)
        food_item.stock -= quantity
        food_item.save()

    # Create order
    order = Order.objects.create(
        customer=user,
        total_price=total_price
    )

    # Add ordered items with quantity (use a Many-to-Many relationship with quantity tracking)
    for item in items:
        food_item = get_object_or_404(FoodItem, id=item['id'])
        OrderItem.objects.create(order=order, food_item=food_item, quantity=item['quantity'])

    return Response({'message': f'Order {order.id} placed successfully!'})
