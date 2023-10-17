def linearSearchProduct(productList, targetProduct):
  indices = []
  for index,  product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["shoes", "boot", "flipflop", "shoes","sandal","shoes"]
target = "shoes"
target2 = 'mango'
result = linearSearchProduct(products, target)
print(result)
