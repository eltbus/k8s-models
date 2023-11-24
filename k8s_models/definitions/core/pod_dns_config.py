from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.pod_dns_config_option import PodDNSConfigOption



class PodDNSConfig(BaseModel):
    nameservers: List[str] = Field(default=None, description=r""" A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. """)
    options: List[PodDNSConfigOption] = Field(default=None, description=r""" A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. """)
    searches: List[str] = Field(default=None, description=r""" A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. """)
