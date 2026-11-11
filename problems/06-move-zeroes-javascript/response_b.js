function moveZeroes(nums) {
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    if (nums[left] === 0) {
      const temp = nums[left];
      nums[left] = nums[right];
      nums[right] = temp;
      right--;
    } else {
      left++;
    }
  }
}
