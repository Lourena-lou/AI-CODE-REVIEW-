#include <algorithm>
#include <vector>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::sort(nums.begin(), nums.end());
    int left = 0;
    int right = static_cast<int>(nums.size()) - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) {
            return {left, right};
        }
        if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {};
}
