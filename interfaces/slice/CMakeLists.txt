# Check the ice binaries


set( SLICE2PY_COMMAND /usr/bin/slice2py)


unset(ICE_FILES CACHE)
FILE(GLOB ICE_FILES "*.ice")

INCLUDE_DIRECTORIES(
  ${CMAKE_CURRENT_SOURCE_DIR}/..
  ${CMAKE_CURRENT_SOURCE_DIR}/../python
  ${ice_path_storm}
  )


FOREACH(currentSourceFile ${ICE_FILES})

  string(REGEX REPLACE ".*/(.*).ice" "\\1.py" SOURCE_PY ${currentSourceFile})

#  message (STATUS "${SLICE2PY_COMMAND} -I${CMAKE_CURRENT_SOURCE_DIR}/.. -I${CMAKE_CURRENT_SOURCE_DIR} --output-dir ${CMAKE_CURRENT_SOURCE_DIR}/../python/ ${currentSourceFile}")

  execute_process(COMMAND ${SLICE2PY_COMMAND} -I${CMAKE_CURRENT_SOURCE_DIR}/.. -I${CMAKE_CURRENT_SOURCE_DIR} --output-dir ${CMAKE_CURRENT_SOURCE_DIR}/../python/ ${currentSourceFile})

  file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/../python/GPS_ice.py DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/../python/tools/)

ENDFOREACH(currentSourceFile)

