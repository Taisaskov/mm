#include<iostream>
using namespace std;
int main() {
	int n, sum;
	int mas[10000];
	sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> mas[i];
		sum += mas[i];
	}
	if (sum % 2 == 1) {
		cout << "NO";
	}
	else {
		cout << "YES";
	}
	return 0;
}