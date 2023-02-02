#include <iostream>
using namespace std;
#include <vector>

int main() {
	vector<int> euclid;

	int cnt = 0;
	for (int i = 0; ; i++) {
		int a, b;

		cin >> a >> b;
		if (a == 0 && b == 0)
			break;
		euclid.push_back(a);
		euclid.push_back(b);

		cnt++;
	}

	for (int i = 0; i < cnt; i++) {
		bool turn = false;

		int a = euclid[i * 2];
		int b = euclid[i * 2 + 1];

		while (1) {
			if (a > b) {
				if (a % b == 0) {
					turn = !turn;
					break;
				}
				else if (a / b == 1) {
					a -= b;
					turn = !turn;
				}
				else {
					turn = !turn;
					break;
				}
			}
			else {
				if (b % a == 0) {
					turn = !turn;
					break;
				}
				else if (b / a == 1) {
					b -= a;
					turn = !turn;
				}
				else {
					turn = !turn;
					break;
				}
			}
		}
		if (turn == true)
			cout << "A wins";
		else
			cout << "B wins";
		if (i != cnt - 1)
			cout << endl;
	}
}