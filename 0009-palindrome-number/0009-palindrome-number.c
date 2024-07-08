int reverse(int number) {
    int t = number, m = 0;
    while (t != 0) {
        if (m > (INT_MAX / 10) || m < (INT_MIN / 10)) {
            // Overflow will happen
            return 0;
        }
        m = m * 10 + t % 10;
        t /= 10;
    }
    return m;
}
bool isPalindrome(int x) {
       if (x < 0) {
        return false;
    }
    return x == reverse(x);
}