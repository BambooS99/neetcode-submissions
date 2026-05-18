class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const stack =[];
        const result = [];
        function backTrack(open,close){
            if (open===n && close===n) {
                return result.push(stack.join('')) ;
            }
            //add to stack
            //call backtrack
            //pop the stack
            //( ) 
            //((()))
            // you can open opening < n

            if(open < n) {
                stack.push('(');
                backTrack(open +1,close);
                stack.pop();
            }
            if (close < open ){
                stack.push(')')
                backTrack(open, close+1);
                stack.pop();
            }
            
        };
        backTrack(0,0);
        return result;
    }

}
