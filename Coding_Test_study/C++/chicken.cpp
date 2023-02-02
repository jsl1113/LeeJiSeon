#include <iostream>
using namespace std;

int main() {
	int tmp = 0, n, k, c = 0;
	while (cin >> n >> k) { //10 3
		tmp = n / (k - 1);
		if (tmp * (k - 1) < n) tmp++;
		c = n + tmp - 1;
		cout << c << endl; //14
	}
	return 0;
}