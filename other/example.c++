#include <bits/stdc++.h>
 
#define X first
#define Y second
#define endl '\n'
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pll;
 
pll operator + (const pll A, const pll B){
    return {A.X + B.X, A.Y + B.Y};
}
 
pll operator - (const pll A, const pll B){
    return {A.X - B.X, A.Y - B.Y};
}
 
ll dot(const pll A, const pll B){
    return A.X * B.X + B.Y * A.Y;
}
 
ll cross(const pll A, const pll B){
    return A.X * B.Y - B.X * A.Y;
}
 
ld dist(pll A, pll B){
    ll dx = A.X - B.X;
    ll dy = A.Y - B.Y;
    return sqrt(dx * dx + dy * dy);
}
 
ll ccw(pll A, pll B, pll C) {
    return A.X * B.Y + B.X * C.Y + C.X * A.Y - A.Y * B.X - B.Y * C.X - C.Y * A.X;
}
 
ld dist2(const pll &x, const pll &y, const pll &z){
    pll t = x + z;
    return 1.0 * abs(cross((y - x), (t - x))) / dist(x, t);
}
 
void convexHull(vector<pll>& v){
    sort(v.begin(), v.end());
    vector<pll> L, R;
    for (const pll& i : v){  // 반복자 개선
        while (L.size() >= 2 && ccw(i, L[L.size() - 1], L[L.size() - 2]) <= 0) L.pop_back();
        L.emplace_back(i);
        while (R.size() >= 2 && ccw(i, R[R.size() - 1], R[R.size() - 2]) >= 0) R.pop_back();
        R.emplace_back(i);
    }
    v.clear();
    for (size_t i = 0; i + 1 < R.size(); i++) {  // 수정된 반복문
        v.emplace_back(R[i]);
    }
    for (size_t i = L.size() - 1; i > 0; i--) {  // 수정된 반복문
        v.emplace_back(L[i]);
    }
}
 
int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
 
    int n; cin >> n;
    vector<pll> v;
    for (int i = 0; i < n; i++){
        ll x, y; cin >> x >> y;
        v.emplace_back(x, y);
    }
    convexHull(v);
    n = v.size();
 
    cout << fixed << setprecision(13);
    if (n == 1) {
        cout << 0;
        return 0;
    }
    if (n == 2){
        cout << 2.0 * dist(v[0], v[1]);
        return 0;
    }
 
    size_t r1 = 1;  // size_t로 변경
    size_t r2 = 1;  // size_t로 변경
    size_t r3 = 1;  // size_t로 변경
    ld ans = 1e16;
    for (size_t i = 0; i < n; i++) {  // size_t로 변경
        if (r1 % n == i) r1++;
        if (r2 % n == i) r2++;
        if (r3 % n == i) r3++;
 
        while (ccw(v[i], v[(i + 1) % n], v[(r1 + 1) % n] - v[r1 % n] + v[(i + 1) % n]) > 0 && dot(v[(i + 1) % n] - v[i], v[(r1 + 1) % n] - v[r1 % n]) > 0) r1++;
        while (ccw(v[i], v[(i + 1) % n], v[(r2 + 1) % n] - v[r2 % n] + v[(i + 1) % n]) > 0) r2++;
        while (ccw(v[i], v[(i + 1) % n], v[(r3 + 1) % n] - v[r3 % n] + v[(i + 1) % n]) > 0 || dot(v[(i + 1) % n] - v[i], v[(r3 + 1) % n] - v[r3 % n]) < 0) r3++;
        pll p = v[(i + 1) % n] - v[i];
        ans = min(ans, (dist2(v[i], v[r2 % n], p) + dist2(v[r1 % n], v[r3 % n], {p.Y, -p.X})) * 2);
    }
    cout << ans;
 
    return 0;
}