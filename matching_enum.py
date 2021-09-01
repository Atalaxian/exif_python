import exif


class MatchingEnum:
    dict_matching = {'orientation': exif.Orientation, 'resolution_unit': exif.ResolutionUnit,
                     'exposure_program': exif.ExposureProgram, 'metering_mode': exif.MeteringMode,
                     'color_space': exif.ColorSpace, 'exposure_mode': exif.ExposureMode,
                     'white_balance': exif.WhiteBalance, 'scene_capture_type': exif.SceneCaptureType,
                     'saturation': exif.Saturation, 'sharpness': exif.Sharpness,
                     'gps_altitude_ref': exif.GpsAltitudeRef, 'light_source': exif.LightSource}