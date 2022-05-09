//Bubblesort algorithms
//Sort algorithms
//bekmuxtorov
//javascript

function bubble(nums){
    for(let i = 0; i < nums.length - 1;i++){
        if(nums[i] > nums[i+1]){
            let num;
            num = nums[i], nums[i+1] = nums[i], nums[i+1] = num;
        }
    }
    return nums;
}

function bubble_sort(nums){
    for(let j=0; j < nums.length - 1; j++){
        bubble(nums);
    }

    return nums;
}



const a_numbers = [10,22,9,64,3];
console.log(bubble_sort(a_numbers))