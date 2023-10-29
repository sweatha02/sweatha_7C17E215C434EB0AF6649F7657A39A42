def linearsearchproduct(productlist,targetproduct):
  indices=[]

  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices

products =["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target1="apple"
result=linearsearchproduct(products,target)
result1=linearsearchproduct(products,target1)
print(result)
print(result1)