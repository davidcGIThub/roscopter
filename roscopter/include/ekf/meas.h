#pragma once

#include <set>
#include <string>

#include <Eigen/Core>

#include <geometry/xform.h>

namespace roscopter
{

namespace ekf
{

namespace meas
{

struct Base
{
    Base();
    virtual ~Base() = default;
    enum
    {
        BASE,
        GNSS,
        IMU,
        MOCAP,
        ZERO_VEL
    };
    double t;
    int type;
    bool handled;
    std::string Type() const;
};

typedef std::multiset<meas::Base*, std::function<bool(const meas::Base*, const meas::Base*)>> MeasSet;
bool basecmp(const Base *a, const Base *b);

struct Gnss : public Base
{
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
    Gnss(double _t, const Vector6d& _z, const Matrix6d& _R);
    Vector6d z;
    Eigen::Map<Eigen::Vector3d> p;
    Eigen::Map<Eigen::Vector3d> v;
    Matrix6d R;
};

struct Imu : public Base
{
    enum
    {
        A = 0,
        W = 3
    };
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
    Imu(double _t, const Vector6d& _z, const Matrix6d& _R);
    Vector6d z;
    Matrix6d R;
};

struct Mocap : public Base
{
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
    Mocap(double _t, const xform::Xformd& _z, const Matrix6d& _R);
    xform::Xformd z;
    Matrix6d R;
};

struct ZeroVel: public Base
{
    ZeroVel(double _t);
};

}

}

}

