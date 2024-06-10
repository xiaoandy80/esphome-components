import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import ICON_MOTION_SENSOR, UNIT_EMPTY
from esphome.const import (
    DEVICE_CLASS_PRESENCE,
    STATE_CLASS_TOTAL,
    CONF_ID,
)


CODEOWNERS = ["@shreyaskarnik","@jsolsona"]
DEPENDENCIES = ["i2c"]

sen21231_sensor_ns = cg.esphome_ns.namespace("sen21231_sensor")
Sen21231Sensor = sen21231_sensor_ns.class_(
    "Sen21231Sensor", cg.PollingComponent, i2c.I2CDevice
)

CONF_PRESENCE = "presence_detected"
CONF_PRESENCE_BOX_CONFIDENCE = "presence_box_confidence"
CONF_PRESENCE_BOX_LEFT = "presence_box_left"
CONF_PRESENCE_BOX_TOP= "presence_box_top"
CONF_PRESENCE_BOX_RIGHT = "presence_box_right"
CONF_PRESENCE_BOX_BOTTOM = "presence_box_bottom"
CONF_PRESENCE_ID_CONFIDENCE = "presence_id_confidence"
CONF_PRESENCE_ID = "presence_id"
CONF_PRESENCE_FACING_CAMERA = "facing_camera"
CONF_PRESENCE_PERSON_NAME = "person_name"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(Sen21231Sensor),
            cv.Optional(CONF_PRESENCE): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_BOX_CONFIDENCE): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_BOX_CONFIDENCE,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_BOX_LEFT): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_BOX_LEFT,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_BOX_TOP): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_BOX_TOP,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_BOX_RIGHT): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_BOX_RIGHT,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_BOX_BOTTOM): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_BOX_BOTTOM,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_ID_CONFIDENCE): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_ID_CONFIDENCE,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_ID): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE_ID,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_FACING_CAMERA): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_PERSON_NAME): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
        }
    )
    .extend(cv.polling_component_schema("30s"))
    .extend(i2c.i2c_device_schema(0x62))
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
#    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    if CONF_PRESENCE in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE])
        cg.add(var.people_detected(sens))
    if CONF_PRESENCE_BOX_CONFIDENCE in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_BOX_CONFIDENCE])
        cg.add(var.people_detected_box_confidence(sens))
    if CONF_PRESENCE_BOX_LEFT in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_BOX_LEFT])
        cg.add(var.people_detected_box_left(sens))
    if CONF_PRESENCE_BOX_TOP in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_BOX_TOP])
        cg.add(var.people_detected_box_top(sens))
    if CONF_PRESENCE_BOX_RIGHT in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_BOX_RIGHT])
        cg.add(var.people_detected_box_right(sens))
    if CONF_PRESENCE_BOX_BOTTOM in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_BOX_BOTTOM])
        cg.add(var.people_detected_box_bottom(sens))
    if CONF_PRESENCE_ID_CONFIDENCE in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_ID_CONFIDENCE])
        cg.add(var.people_detected_id_confidence(sens))
    if CONF_PRESENCE_ID in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_ID])
        cg.add(var.people_detected_id(sens))
    if CONF_PRESENCE_FACING_CAMERA in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_FACING_CAMERA])
        cg.add(var.people_detected_facing_camera(sens))
    if CONF_PRESENCE_PERSON_NAME in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_PERSON_NAME])
        cg.add(var.people_detected_person_name(sens))
