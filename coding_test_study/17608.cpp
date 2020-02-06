#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	int result = 1;
	int m = arr[n - 1];
	for (int i = n-2; i >= 0; i--) {
		if (m < arr[i]) {
			result++;
			m = arr[i];
		}
	}
	cout << result;
}