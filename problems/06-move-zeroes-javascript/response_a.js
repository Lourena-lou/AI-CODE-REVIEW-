function moveZeroes(nums) {
  let insert = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      const temp = nums[insert];
      nums[insert] = nums[i];
      nums[i] = temp;
      insert++;
    }
  }
}
