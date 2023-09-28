def linearSearchProduct(productList,targetProduct):
  indices = []
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
prod = ["keyboard", "printer", "mouse", "keyboard", "touchpad", "keyboard"]
tar = "keyboard"
res = linearSearchProduct(prod,tar)
print(res)
