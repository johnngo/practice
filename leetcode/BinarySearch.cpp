// Binary search is a textbook algorithm based on the idea
// to compare the value to the middle element of the array
// If the target value is equal to the middle element - we're done
// if the target value is smallar - continue to search on the left
// if the taget value is larget - continue to search on the right


class Solution{
  public:
  int search(vector<int>& nums, int target) {
    int pivot, left =0, right = nums.size() - 1;
    while(left <=right) {
      pivot = left + (right - left) /2;
      if(nums[pivot] ==target) return pivot;
      if(target < nums[pivot]) right = pivot - 1;
      else left = pivot + 1;
    }
    return -1;
  }
};
