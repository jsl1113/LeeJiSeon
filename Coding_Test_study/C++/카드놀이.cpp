#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
   int T, N;

   cin >> T;  // 테스트 케이스 개수 
   

   for (int i = 0; i < T; i++) {
      cin >> N; // 카드 개수
      

      vector<int> card(N);
      vector<int> even;
      vector<int> odd;
      int sum = 0;


      for (int i = 0; i < N; i++) {
         cin >> card[i];   // 카드 입력 받음
         if (card[i] % 2 == 0)
            even.push_back(card[i]);
         else
            odd.push_back(card[i]);
      }
      sort(card.begin(), card.end());
      sort(even.begin(), even.end());
      sort(odd.begin(), odd.end());



      for (int i = 0; i < even.size() / 2; i++) 
         sum += even[even.size()-i-1];

            
      for (int i = 0; i < odd.size() / 2; i++)
         sum += odd[odd.size() - i - 1];


      if (even.size() % 2 != 0) {
         if (even[even.size() / 2] > odd[odd.size() / 2])
            sum += odd[odd.size() / 2];
         else
            sum += even[even.size() / 2];
      }

      cout << sum << endl;
   }
   

   return 0;                     
}