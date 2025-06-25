#include <limits.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool helper(struct TreeNode* root, long min, long max){
    if(!root){return true;}
    //invalid condition
    if(root->val <= min || root->val >= max){return false;}
    return helper(root->right, root->val, max) && helper(root->left, min, root->val);

}
bool isValidBST(struct TreeNode* root) {
    // Some recursion when checking left and right
    // MY BASIC INTUITTION FAILED TO CHECK THE WHOLE TREE 
    // Need to pass along a range to keep checking 

    //RECURSION OPTIMAL
    return helper(root, LONG_MIN, LONG_MAX);

    // // BASE CASE : 
    // //1. NO ROOT
    // if (!root){return true;}
    // //2. If there's only single node i.e., left and right are empty then, valid
    // if (!root->left && !root->right){
    //     return true;
    // } 
    // //3. If left empty but right not then, check right value and just call recursive
    // if(!root->left && root->right){
    //     if (root->val < root->right->val){
    //         return isValidBST(root->right);
    //     }else{return false;}
    // }
    
    // //4. If right empty but left not then, check right value and just call recursive
    // if(!root->right && root->left){
    //     if (root->val > root->left->val){
    //         return isValidBST(root->left);
    //     }else{return false;}
    // }

    // // if both are not empty 
    // if (root->val < root->right->val && root->val > root->left->val){
    //         return (isValidBST(root->right) && isValidBST(root->left));
    // }
    // return false;
}