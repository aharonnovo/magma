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

from .location_fragment import LocationFragment, QUERY as LocationFragmentQuery

@dataclass
class LocationChildrenQuery(DataClassJsonMixin):
    @dataclass
    class LocationChildrenQueryData(DataClassJsonMixin):
        @dataclass
        class Node(DataClassJsonMixin):
            @dataclass
            class Location(LocationFragment):
                pass

            children: List[Location]

        location: Optional[Node]

    data: LocationChildrenQueryData

    __QUERY__: str = LocationFragmentQuery + """
    query LocationChildrenQuery($id: ID!) {
  location: node(id: $id) {
    ... on Location {
      children {
        ...LocationFragment
      }
    }
  }
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, id: str) -> LocationChildrenQueryData:
        # fmt: off
        variables = {"id": id}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data
