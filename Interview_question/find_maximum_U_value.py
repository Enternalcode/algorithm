"""
Rearrange an array of integers so that the calculated value U is maximized. Among the
arrangements that satisfy that test, choose the array with minimal ordering. The value of U
for an array with n elements is calculated as :
U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×arr[n-1] × (1÷arr[n]) if n is odd
or
U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×(1÷arr[n-1]) × arr[n] if n is even
The sequence of operations is the same in either case, but the length of the array, n,
determines whether the calculation ends on arr[n] or (1÷arr[n]).
Arrange the elements to maximize U and the items are in the numerically smallest possible
order.
"""

# example_arrs = [21, 34, 5, 7, 9]

"""
According to the title, we need to reach two conditions
Condition 1: Find the largest U-value
Condition 2: If condition 1 is met, sort the list in the smallest order

Analyzing the equation for U shows that:
1. All elements are multiplied, so if the value of an element is fixed,
changing the position of an element in the equation will not change the result.
2. From 1, the size of the result U depends on the size of the elemnts in the equation
3. Further, it is clear from the equation that the size of an element is determined only by its position,
starting at the odd bits of the equation(from the index bit index >= 2), the element is changed to
(1/element itself), and remains unchanged at the event bits, so to find the largest U, one should make
the elements at  these odd bits as large as possible.
4. By the nature of division, 1 / x should be as large as possible, so the base x should be as small as possbile,
so you should use the smallest element of the list as the x-value as much as possible
5. In analyzing the equation from the question, it is clear that the number of elements that need to be converted
to their own fractions m:
m =  {
    0, n <=2,
	(n - 3) / 2 + 1 , n>2, if n is odd
	(n-2) /  2, n>2, if n is even
}
"""

from typing import List, Union


class Source:
    len_2_test_arrs = [21, 34]
    odd_len_test_arrs = [21, 34, 5, 7, 9]
    event_len_test_arrs = [21, 34, 5, 7, 9, 2]


class Test:
    def calculate_U(self, arrs: List[int]) -> Union[int, float]:
        n = len(arrs)
        U = arrs[0] * arrs[1]
        # * Index = arithmetic expression actual position - 1, not the same
        # * transfer operation
        for  i in range(2, n):
            if i % 2 == 0:
                U /= arrs[i]
            else:
                U *= arrs[i]
        print('The result U is calculated as: ', U)        
        return U            

    def test_solution_v0(self):
        s_v0 = SolutionV0()
        result = s_v0.main(Source.odd_len_test_arrs)
        self.calculate_U(result)


class SolutionV0:
    def __init__(self) -> None:
        pass

    def main(self, arrs: List[int]) -> List[int]:
        print("origin arrs", arrs)
        # Arrange the array from smallest to largest first
        arrs.sort()
        print("After sorting from small to large", arrs)

        # Determine the total length of the array
        length_of_arrs = len(arrs)
        print("total length of arrs", length_of_arrs)

        # Conditional processing based on array length
        if length_of_arrs <= 2:
            print("length less than 2, directly return")
            return length_of_arrs

        # When the length is greater than 2

        # Determine if the total length is odd or even
        # m indicates how many elements will need to be converted to their own fraction
        result = []
        if length_of_arrs % 2 == 1:
            # odd
            m = (length_of_arrs - 3) / 2 + 1

        else:
            # even
            m = (length_of_arrs - 2) / 2

        # Remove the first m elements of the arrs
        m = int(m) # * Division may cause m to become a floating point number
        fractional_element_list = arrs[:m]
        remaining_element_list = arrs[m:]

        # Insert the elements to be converted into fractions into the odd positions
        # of the  list of remaining elements, starting at position 3 (index = 2)
        index = 2
        for i, element in enumerate(fractional_element_list):
            remaining_element_list.insert(index, element)
            index += 2
        result = remaining_element_list
        print("result list", result)
        return result


if __name__ == "__main__":
    test = Test()
    test.test_solution_v0()
