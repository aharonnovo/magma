/**
 * Copyright 2004-present Facebook. All Rights Reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @flow strict-local
 * @format
 */

import type {ViewContainerProps} from '@fbcnms/ui/components/design-system/View/ViewContainer';

import * as React from 'react';
import ListAltIcon from '@material-ui/icons/ListAlt';
import MapIcon from '@material-ui/icons/Map';
import ViewContainer from '@fbcnms/ui/components/design-system/View/ViewContainer';
import {VARIANTS} from '@fbcnms/ui/components/design-system/View/ViewBody';
import {makeStyles} from '@material-ui/styles';
import {useState} from 'react';

const useStyles = makeStyles(() => ({
  root: {
    display: 'flex',
    height: '100%',
  },
}));

export const DisplayOptions = {
  table: 'table',
  map: 'map',
};
export type DisplayOptionTypes = $Keys<typeof DisplayOptions>;

type ViewToggleProps = {
  onViewToggleClicked?: (id: string) => void,
};

type Props = ViewContainerProps & ViewToggleProps;

const InventoryView = (props: Props) => {
  const {onViewToggleClicked, ...restProps} = props;
  const viewProps: ViewContainerProps = {
    ...restProps,
  };
  const classes = useStyles();
  const [selectedDisplayOption, setSelectedDisplayOption] = useState(
    DisplayOptions.table,
  );
  if (selectedDisplayOption == DisplayOptions.map) {
    viewProps.bodyVariant = VARIANTS.plain;
  }
  if (viewProps.header && onViewToggleClicked) {
    const onViewOptionClicked = displayOptionId => {
      setSelectedDisplayOption(displayOptionId);
      if (onViewToggleClicked) {
        onViewToggleClicked(displayOptionId);
      }
    };
    viewProps.header.viewOptions = {
      onItemClicked: onViewOptionClicked,
      selectedButtonId: selectedDisplayOption,
      buttons: [
        {
          item: <ListAltIcon />,
          id: DisplayOptions.table,
        },
        {
          item: <MapIcon />,
          id: DisplayOptions.map,
        },
      ],
    };
  }
  return (
    <div className={classes.root}>
      <ViewContainer {...viewProps} />
    </div>
  );
};

export default InventoryView;
