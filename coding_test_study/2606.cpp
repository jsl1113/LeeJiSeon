#include <iostream>
using namespace std;
int main() {
	int computer, n;
	cin >> computer;
	cin >> n; 
	int** arr = new int*[n];
	for (int i = 0; i < n; i++)
		arr[i] = new int[n];
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		arr[x][y] = 1;
		arr[y][x] = 1;
		arr[x][x] = 1;
		arr[y][y] = 1;
	}
}