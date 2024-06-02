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
CONF_PRESENCE_FORWARD = "facing_forward"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(Sen21231Sensor),
            cv.Optional(CONF_PRESENCE): sensor.sensor_schema(
#                device_class=DEVICE_CLASS_PRESENCE,
                state_class=STATE_CLASS_TOTAL,
                icon=ICON_MOTION_SENSOR, accuracy_decimals=1,
            ),
            cv.Optional(CONF_PRESENCE_FORWARD): sensor.sensor_schema(
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

    if CONF_PRESENCE_FORWARD in config:
        sens = await sensor.new_sensor(config[CONF_PRESENCE_FORWARD])
        cg.add(var.people_detected_facing_forward(sens))