#include <iostream>
#include <string>
using namespace std;

int n;
string word[100];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> word[i];
	}

	for (int i = 0; i < n; i++) {
		string s = word[i];
		if (s.length() > 10) {
			cout << s[0] << s.length() - 2 << s[s.length() - 1] << '\n';
		}
		else {
			cout << s << '\n';
		}
	}
}