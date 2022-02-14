import lab2


if __name__ == 'main':
    lab2.initialize()

    lab2.add(40)
    if lab2.get_current_value() == 40:
      print("Test 1 passed")
    else:
      print("Test 1 failed")

    lab2.divide(2)
    if lab2.get_current_value()==20:
      print("Test 2 passed")
    else:
      print("Test 2 failed")

    lab2.multiply(3)
    if lab2.get_current_value()==60:
      print("Test 3 passed")
    else:
      print("Test 3 failed")

    lab2.undo()
    if lab2.get_current_value()==20:
      print("Test 4 passed")
    else:
      print("Test 4 failed")

    lab2.commitToMemory()
    lab2.add(10)
    lab2.recall()
    if lab2.get_current_value()==20:
      print("Test 5 passed")
    else:
      print("Test 5 failed")

    lab2.undo()
    if lab2.get_current_value()==30:
      print("Test 6 passed")
    else:
      print("Test 6 failed")