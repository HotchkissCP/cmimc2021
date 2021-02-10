#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int,int> pi;
typedef vector<pi> vpi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = a; i <= b; i++)
#define TRAV(a, x) for (auto& a : x)

void setIO(string name) {
    //ios_base::sync_with_stdio(0); cin.tie(0);
    freopen((name+".in").c_str(),"r",stdin);
    //freopen((name+".out").c_str(),"w",stdout);
}

void setIO() {
    ios_base::sync_with_stdio(0); cin.tie(0);
}

bool in_circle(int radius, int pointX, int pointY, int centerX, int centerY) {
  double distance = sqrt((pointX-centerX)*(pointX-centerX) + (pointY - centerY)*(pointY - centerY));
  return distance <= radius * 1.0;
}

vector<vi> established_circles;

bool is_overlapping(int r1, int x1, int y1) {
  TRAV(circle, established_circles) {
    if (sqrt((x1-circle[1])*(x1-circle[1]) + (y1-circle[2])*(y1-circle[2])) < 0.0 + r1 + circle[0]) {
      return true;
    }
  }
  return false;
}


int main() {
    setIO("circlecovers5");

    int n;
    cin >> n;

    int maxx = 0, maxy = 0, minx = 9999, miny = 9999;

    vector<vi> grid;
    vector<vector<bool>> to_skip;
    REP(i, 0, 2000 - 1) {
      vi row;
      vector<bool> srow;
      grid.PB(row);
      to_skip.PB(srow);
      REP(j, 0, 2000 - 1) {
        grid[i].PB(0);
        to_skip[i].PB(false);
      }
    }

    vpi points;
    REP(i, 1, n) {
      int p1, p2;
      cin >> p1 >> p2;
      if (p1 > maxx) {
        maxx = p1;
      }
      if (p1 < minx) {
        minx = p1;
      }
      if (p2 > maxy) {
        maxy = p2;
      }
      if (p2 < miny) {
        miny = p2;
      }
      points.PB(MP(p1,p2));
      grid[p1][p2]++;
    }

    vpi to_consider;
    REP(i, minx, maxx) {
      REP(j, miny, maxy) {
        to_consider.PB(MP(i,j));
      }
    }
    // cout << maxx << " " << minx << " " << maxy << " " << miny << "\n";
    // TRAV(a, to_consider) {
    //   cout << a.F << " " << a.S << "\n";
    // }
    // REP(i, 0, 2000 - 1) {
    //   REP(j, 0, 2000 - 1) {
    //     cout << grid[i][j] << " ";
    //   }
    //   cout << "\n";
    // }
    int m;
    cin >> m;
    vi radii;
    vi radii_sorted;
    REP(i, 1, m) {
      int r;
      cin >> r;
      radii.PB(r);
      radii_sorted.PB(r);
    }

    sort(radii_sorted.rbegin(),radii_sorted.rend());

    int counter = 0;

    TRAV(r, radii_sorted) {
      cout << counter << " " << r << "\n";
      counter++;

      pi most_dense = MP(0, 0);
      int max_points = 0;

      TRAV(point, to_consider) {
        int x = point.F;
        int y = point.S;
        if (to_skip[x][y]) {
          continue;
        }
        int points_in_circle = 0;
        if (!is_overlapping(r, x, y)) {
          REP(px, max(0, x - r), min(x + r, 2000 - 1)) {
            REP(py, max(0, y - r), min(y + r, 2000 - 1)) {
              // cout << px << " " << py << "\n";
              if (in_circle(r, px, py, x, y)) {
                points_in_circle += grid[px][py];

              }
            }
          }
          if (points_in_circle > max_points) {
            max_points = points_in_circle;
            most_dense = point;
          }
          if (points_in_circle == 0) {
            to_skip[x][y] = true;
          }
          // TRAV(p, points) {
          //   int px = p.F;
          //   int py = p.S;
          //   if (in_circle(r, px, py, x, y)) {
          //     points_in_circle++;
          //     if (points_in_circle > max_points) {
          //       max_points = points_in_circle;
          //       most_dense = point;
          //     }
          //   }
          // }
        }
      }

      vi circle = {r, most_dense.F, most_dense.S};
      established_circles.PB(circle);
    }

    TRAV(r, radii) {
      REP(i, 0, m - 1) {
        if (established_circles[i][0] == r) {
          vi circle = established_circles[i];
          cout << circle[1] << ".0 " << circle[2] << ".0\n";
          established_circles.erase(established_circles.begin() + i);
          break;
        }
      }
    }
    // TRAV(a, established_circles) {
    //   TRAV(b, a) {
    //     cout << b << " ";
    //   }
    //   cout << "\n";
    // }
}
