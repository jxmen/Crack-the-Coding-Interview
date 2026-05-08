/**

    현재 주식 가격에서 뒤에 있는 주식 가격의 최대값 만큼의 차액이 최대 이익이 된다.

    [1,2,3,4] i=0 -> arr[3] - arr[i] = 3

    [1,5,2,3] arr[1] - arr[0] = 4

 */

class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxProfit = 0;
        int maxPrice = 0;

        for (int i = n-1; i > -1; i--) {
            int price = prices[i];

            maxProfit = Math.max(maxProfit, maxPrice - price);
            maxPrice = Math.max(maxPrice, price);    
        }

        return maxProfit;
    }
}
