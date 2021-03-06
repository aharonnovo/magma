#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin

from .customer_fragment import CustomerFragment, QUERY as CustomerFragmentQuery

@dataclass
class CustomersQuery(DataClassJsonMixin):
    @dataclass
    class CustomersQueryData(DataClassJsonMixin):
        @dataclass
        class CustomerConnection(DataClassJsonMixin):
            @dataclass
            class CustomerEdge(DataClassJsonMixin):
                @dataclass
                class Customer(CustomerFragment):
                    pass

                node: Optional[Customer]

            edges: List[CustomerEdge]

        customers: Optional[CustomerConnection]

    data: CustomersQueryData

    __QUERY__: str = CustomerFragmentQuery + """
    query CustomersQuery {
  customers {
    edges {
      node {
        ...CustomerFragment
      }
    }
  }
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient) -> CustomersQueryData:
        # fmt: off
        variables = {}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data
