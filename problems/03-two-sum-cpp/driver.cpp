#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> twoSum(std::vector<int>& nums, int target);

int main() {
    int cases;
    if (!(std::cin >> cases)) {
        return 0;
    }
    for (int c = 0; c < cases; ++c) {
        int n;
        int target;
        std::cin >> n >> target;
        std::vector<int> nums(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> nums[i];
        }
        std::vector<int> before = nums;
        std::vector<int> result = twoSum(nums, target);
        int mutated = (nums != before) ? 1 : 0;
        if (result.size() == 2) {
            int a = result[0];
            int b = result[1];
            if (a > b) {
                std::swap(a, b);
            }
            std::cout << a << " " << b << " " << mutated << "\n";
        } else {
            std::cout << "none -1 " << mutated << "\n";
        }
    }
    return 0;
}
