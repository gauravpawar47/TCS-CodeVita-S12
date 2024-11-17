#include <bits/stdc++.h>
using namespace std;

int main() {
    int b, n, cb = 0;
    cin >> b >> n;
    vector<int> t;
    vector<int> cs = {b};

    for (int i = 0; i < n; i++) {
        string placementlelo;
        cin >> placementlelo;

        if (placementlelo == "read") {
            cout << cs[cb] << endl;
        } else if (placementlelo == "credit" || placementlelo == "debit") {
            int x;
            cin >> x;
            if (placementlelo == "credit")
                cs[cb] += x;
            else
                cs[cb] -= x;
            t.push_back(placementlelo == "credit" ? x : -x);
        } else if (placementlelo == "abort") {
            int x;
            cin >> x;
            if (x <= t.size()) {
                cs[cb] -= t[x - 1];
                t[x - 1] = 0;
            }
        } else if (placementlelo == "rollback") {
            int x;
            cin >> x;
            cb = x - 1;
            cs.resize(cb + 1);
        } else if (placementlelo == "commit") {
            cs.push_back(cs[cb]);
            cb++;
        }
    }

    return 0;
}
