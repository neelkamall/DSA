function singleNumber(nums: number[]): number {
    let single: number = 0;
    for (let num of nums) {
        single ^= num;
    }
    return single;
    
};