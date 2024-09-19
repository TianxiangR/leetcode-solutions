/*
 * @lc app=leetcode id=2215 lang=typescript
 *
 * [2215] Find the Difference of Two Arrays
 */

// @lc code=start
// @ts-ignore
declare global {
  interface Set<T> {
      difference(otherSet: Set<T>): Set<T>;
  }
}

interface Set<T> {
  difference(otherSet: Set<T>): Set<T>;
}

Set.prototype.difference = function<T>(this: Set<T>, otherSet: Set<T>) {
  const diff = new Set();
  this.forEach((value) => {
    if (!otherSet.has(value)) {
      diff.add(value);
    }
  });

  return diff;
}

function findDifference(nums1: number[], nums2: number[]): number[][] {
    const set1 = new Set(nums1), set2 = new Set(nums2);

    return [[...set1.difference(set2)], [...set2.difference(set1)]]
};
// @lc code=end

