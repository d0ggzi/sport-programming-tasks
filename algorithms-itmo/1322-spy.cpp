#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int n, len;
    string s;
    cin >> n >> s;
    len = s.size();
    pair<int, char> dict[len];

    for (int i = 0; i < len; i++){
        dict[i].first = i;
        dict[i].second = s[i];
    }
    sort(dict, dict + len, [](const pair<int, char>& x1, const pair<int, char>& x2) -> bool {
        return x1.second < x2.second;
    });

    n = n - 1;
    for (int i = 0; i < len; i++) {
        n = dict[n].first;
        cout << s[n];
    }

    return 0;
}