# Define the package resource to install Flask using the system package manager
package { python3-pip:
  ensure => installed,
}

package { flask:
  ensure   => 2.1.0,      # Ensure specific version 2.1.0 is installed
  provider => pip3,       # Use pip3 provider for installation
}
