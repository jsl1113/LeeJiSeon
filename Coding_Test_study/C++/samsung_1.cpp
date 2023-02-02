#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int T, test_case;
int Answer;
int f;
int arr[100001];
bool visit[100001];
queue<int> Q;

int main(int argc, char** argv) {
    //freopen("input.txt", "r", stdin);

    cin >> T;
    for (test_case = 0; test_case < T; test_case++) {
        Answer = 0;
        cin >> f;

        int fn;
        for (int i = 1; i <= f; i++) {
            cin >> fn;
            arr[i] = i + fn;
            visit[i] = false;
        }

        for (int i = 1; i <= f; i++) {
            if (visit[i]) continue;
            Q.push(i);
            visit[i] = true;
            bool b = true;

            while (!Q.empty()) {
                int tmp = Q.front();
                Q.pop();
                if (arr[tmp] > f) continue;
                if (visit[arr[tmp]]) {
                    b = false;
                    break;
                }
                Q.push(arr[tmp]);
                visit[arr[tmp]] = true;
            }
            if (b) Answer++;
        }
        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
    }
    return 0;
}