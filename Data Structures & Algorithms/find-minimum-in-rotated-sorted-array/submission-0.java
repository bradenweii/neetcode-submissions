class Solution {
    public int findMin(int[] nums) {
        int low=0;
        int high=nums.length-1;
        while(low<high){
            int mid = (low+high)/2;
            if(arr[low]<arr[high]){
                return arr[low];
            }
            if(arr[mid]>arr[high]){
                low=mid+1;
            }else{
                high=mid;
            }
        }
        return arr[low];
    }
}
