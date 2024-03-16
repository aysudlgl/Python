function linearSearch(array, key){
  for(let i = 0; i < array.length; i++){
    if(array[i] === key) {
        return i;
    }
  }
  return -1;
}
console.log(linearSearch([1,2,3,4,5],4));
//binary search
function binarySearch(array, key) {
    let left = 0;
    let right = array.length - 1;
    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        if (array[mid] === key) {
            return mid;
        }
        if (array[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
console.log(binarySearch([0,1,2,3,4,5,6,7,8],8))