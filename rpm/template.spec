Name:           ros-kinetic-summit-xl-sim-bringup
Version:        1.0.9
Release:        0%{?dist}
Summary:        ROS summit_xl_sim_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/summit_xl_sim_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-summit-xl-control
Requires:       ros-kinetic-summit-xl-description
Requires:       ros-kinetic-summit-xl-pad
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roslaunch

%description
Launch files for Summit XL simulation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Jul 13 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.9-0
- Autogenerated by Bloom

