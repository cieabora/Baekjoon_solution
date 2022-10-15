#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int key) {
   int left, mid, right;
   left = 0, right = n - 1;
   while (left <= right) {
      mid = (left + right) / 2;
      if (arr[mid] == key) return 0;
      else if (arr[mid] < key) left = mid + 1;
      else right = mid - 1;
   }
   return -1;
}
int cmp(const void* a, const void* b) {
   return *(int*)a > * (int*)b ? 1 : (*(int*)a < *(int*)b ? -1 : 0);
}
int main(void) {
   int n, g;
   int k[100000];
   int num;
   cin >> n;
   for (int i = 0; i < n; i++) {
       cin >> k[i];
   }
   cin >> g;
   qsort(k, n, sizeof(int), cmp);
   for (int i = 0; i < g; i++) {
      cin >> num;
      if (binarySearch(k, n, num) == 0) cout << 1 << '\n';
      else cout << 0 << '\n';
   }
   return 0;
}