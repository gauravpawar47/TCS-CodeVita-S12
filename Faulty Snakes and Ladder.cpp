#include <bits/stdc++.h>  
using namespace std;  
  
#define loop(i, a, n) for (lli i = (a); i < (n); ++i)  
#define loopD(i, a, n) for (lli i = (a); i >= (n); --i)  
#define all(c) (c).begin(), (c).end()  
#define rall(c) (c).rbegin(), (c).rend()  
#define sz(a) ((int)a.size())  
#define YES cout << "YES";  
#define NO cout << "NO";  
#define endl '\n'  
#define fastio std::ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);  
#define pb push_back  
#define pp pop_back()  
#define fi first  
#define si second  
#define v(a) vector<int>(a)  
#define vv(a) vector<vector<int>>(a)  
#define present(c, x) ((c).find(x) != (c).end())  
#define set_bits __builtin_popcountll  
#define MOD 1000000007  
#define int long long  
  
typedef long long lli;  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef pair<lli, lli> pll;  
typedef pair<int, int> pii;  
typedef unordered_map<int, int> umpi;  
typedef map<int, int> mpi;  
typedef vector<pii> vp;  
typedef vector<lli> vll;  
typedef vector<vll> vvll;  
  
struct game {  
    int start;  
    int end;  
    string type;  
};  

bool solve(vector<int>& dieRolls, unordered_map<int, int>& board, int finalPos) {  
    int position = 1;  
    for (int roll : dieRolls) {  
        if (position + roll <= 100) {  
            position += roll;  
        }  
        while (board.find(position) != board.end()) {  
            position = board[position];  
        }  
    }  
    if (board.find(position) != board.end()) {  
        return false;  
    }  
    return position == finalPos;  
}  

void solve()  
{  
    int N;  
    cin >> N;  
    vector<game> snakesLadders;  
    unordered_map<int, int> board;  
    for (int i = 0; i < N; ++i) {  
        int start, end;  
        cin >> start >> end;  
        game sl;  
        sl.start = start;  
        sl.end = end;  
        if (start > end) {  
            sl.type = "Snake";  
        } else {  
            sl.type = "Ladder";  
        }  
        snakesLadders.push_back(sl);  
        board[start] = end;  
    }  

    vector<int> remainingInput;  
    int num;  
    while (cin >> num) {  
        remainingInput.push_back(num);  
    }  
    if (remainingInput.empty()) {  
        cout << "Not reachable";  
        return;  
    }  
    int finalPos = remainingInput.back();  
    remainingInput.pop_back();  
    vector<int> dieRolls = remainingInput;  
  
    if (solve(dieRolls, board, finalPos)) {  
        cout << "Not affected";  
        return;  
    }  

    for (size_t i = 0; i < snakesLadders.size(); ++i) {  
        game& sl = snakesLadders[i];  
        board.erase(sl.start);  
        int newStart = sl.end;  
        int newEnd = sl.start;  
        string newType = (sl.type == "Snake") ? "Ladder" : "Snake";  
        if (newStart == 1 || board.find(newStart) != board.end()) {  
            board[sl.start] = sl.end;  
            continue;  
        }  
        board[newStart] = newEnd;  
        if (solve(dieRolls, board, finalPos)) {  
            cout << newType << " " << newStart << " " << newEnd;  
            return ;  
        }  
        board.erase(newStart);  
        board[sl.start] = sl.end;  
    }  
  
    cout << "Not reachable";  
    return ;  
}  

int32_t main()  
{  
    int tc = 1;  
    while (tc--)  
    {  
        solve();  
    }  
    return 0;  
}
