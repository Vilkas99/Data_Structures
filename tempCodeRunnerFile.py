     print("Runner_2:", runner2.value)
                headReference = runner2
                runner2 = runner2.next_value
                print("Runner_2 _NEXT TIME_:", runner2.value)
                headReference.next_value = runner1

                print("Runner_1:", runner1.value)
                valueReference = runner1
                runner1 = runner1.next_value
                print("Runner_1 _NEXT TIME_ :", runner1.value)
                valueReference.next_value = runner2