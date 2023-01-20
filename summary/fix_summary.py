from __future__ import annotations

import os
from typing import Any

import tensorflow as tf
from tensorflow.core.util.event_pb2 import Event

from summary import AnyPath, ProtoEvent, TFRecordDataset


def fix_events(input_path: AnyPath, output_path: AnyPath) -> None:
    # Make a record writer
    with tf.io.TFRecordWriter(output_path) as writer:
        # Alias
        writer: tf.io.TFRecordWriter | Any = writer
        # Iterate event records
        ds: TFRecordDataset | Any = tf.data.TFRecordDataset([input_path])
        prev_value = 0.0
        for record in ds:
            # Alias
            ev: ProtoEvent | Any = Event()
            # Read event
            ev.MergeFromString(record.numpy())
            # Check if it is a summary
            if ev.summary:
                # Iterate summary values
                for v in ev.summary.value:
                    # Check if the tag should be renamed
                    if v.tag == 'train/cls_loss':
                        if v.simple_value > 1000:
                            print(f'Found bad value: {v.simple_value} at step {ev.step}! Replacing with {prev_value}.')
                            v.simple_value = prev_value
                        prev_value = v.simple_value
            writer.write(ev.SerializeToString())


def main() -> None:
    name = "YOLOv6\\runs\\train\\exp2\\events.out.tfevents.1674171716.DESKTOP-I1Q6GKF.20044.0"
    temp_name = 'temp_events'
    fix_events(name, temp_name)
    os.replace(temp_name, name)


if __name__ == '__main__':
    main()
